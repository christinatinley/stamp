import axios from 'axios';

const state = {
    formData: {
        destination: '',
        startDate: '',
        endDate: '',
        budget: '',
        blockedTimes: {},
        numberOfTravelers: '',
        lodging: '',
        cuisines: [],
        dietaryRestrictions: [],
        experiences: [],
      },
    itinerary: [],
}   

const getters = {
    formData: (state) => state.formData,
    itinerary: (state) => state.itinerary,
}

const actions = {
    async fetchHome() {
        try {
            const response = await axios.get('http://127.0.0.1:5000/');
        } catch (error) {
            console.error('Error fetching home data:', error);
        }
    },

    async fetchItinerary({state, commit}) {
      try {
        const personaData = {
            start_day: formatDate(state.formData.startDate),
            end_day: formatDate(state.formData.endDate),
            culture: state.formData.experiences['exploring local culture'] || 0,
            history: state.formData.experiences['historical sites & museums'] || 0,
            art: state.formData.experiences['art sites & museums'] || 0,
            nature: state.formData.experiences['nature exploration'] || 0,
            walking_tours: state.formData.experiences['tours'] || 0,
            shopping: state.formData.experiences['shopping'] || 0,
            price_level: state.formData.budget,
            breaks: Object.values(state.formData.blockedTimes).map(times => {
                const start = formatDateTime(times.start);
                const end = formatDateTime(times.end);  
                return `${start}–${end}`;
            })
        }

        const response = await axios.post('http://127.0.0.1:5000/itinerary', {
            city_name: state.formData.destination,
            persona: personaData,
        });

        const itineraryData = response.data;
        const parsedItinerary = itineraryData.map(dayObj => {
            const newDayObj = {};
            for (const [time, infoString] of Object.entries(dayObj)) {
              newDayObj[time] = parsePlaceInfo(infoString);
            }
            return newDayObj;
        });
        commit('setItinerary', parsedItinerary);
        return response.data;
      } catch (error) {
        console.error('Error fetching itinerary:', error);
        throw error;
      }
    },

    setDestination({ commit }, destination) {
      commit('updateDestination', destination);
    },
    setStartDate({ commit }, startDate) {
      commit('updateStartDate', startDate);
    },
    setEndDate({ commit }, endDate) {
      commit('updateEndDate', endDate);
    },
    setBudget({ commit }, budget) {
      commit('updateBudget', budget);
    },
    setBlockedTimes({ commit }, payload) {
      commit('updateBlockedTimes', payload);
    },
    setNumberOfTravelers({ commit }, numberOfTravelers) {
      commit('updateNumberOfTravelers', numberOfTravelers);
    },
    setLodging({ commit }, lodging) {
      commit('updateLodging', lodging);
    },
    setCuisine({ commit }, cuisine) {
      commit('updateCuisine', cuisine);
    },
    setDietaryRestrictions({ commit }, dietaryRestriction) {
      commit('updateDietaryRestrictions', dietaryRestriction);
    },
    setExperiences({ commit }, payload) {
      commit('updateExperiences', payload);
    }
  };
  

const mutations = {
    updateDestination(state, destination) {
        state.formData.destination = destination;
    },
    updateStartDate(state, startDate) {
        state.formData.startDate = startDate;
    },
    updateEndDate(state, endDate) {
        state.formData.endDate = endDate;
    },
    updateBudget(state, budget) {
        state.formData.budget = budget;
    },
    updateBlockedTimes(state, { date, times }) {
        state.formData.blockedTimes = {
          ...state.formData.blockedTimes,
          [date]: times,
        };
    },
    updateNumberOfTravelers(state, numberOfTravelers) {
        state.formData.numberOfTravelers = numberOfTravelers;
    },
    updateLodging(state, lodging) {
        state.formData.lodging = lodging;
    },
    updateCuisine(state, cuisine) {
        state.formData.cuisines = cuisine;
    },
    updateDietaryRestrictions(state, dietaryRestriction) {
        state.formData.dietaryRestrictions = dietaryRestriction;
    },
    updateExperiences(state, {experience, rating}) {
        state.formData.experiences = {
            ...state.formData.experiences,
            [experience]: rating,
        };
    },
    setItinerary(state, itinerary) {
        state.itinerary = itinerary;
    },
}

function formatDateTime(date) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0'); // months are 0-indexed
    const day = String(date.getDate()).padStart(2, '0');
    const hour = String(date.getHours()).padStart(2, '0');
    const minute = String(date.getMinutes()).padStart(2, '0');
    return `${year}-${month}-${day} ${hour}:${minute}`;
}

function formatDate(date) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0'); // months are 0-based
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
  }

  function parsePlaceInfo(placeString) {
    const lines = placeString.split('\n').map(line => line.trim()).filter(Boolean);
    const result = {};
  
    lines.forEach(line => {
      const [key, ...rest] = line.split(':');
      const value = rest.join(':').trim();
  
      switch (key) {
        case 'Place Name':
          result.placeName = value;
          break;
        case 'Address':
          result.address = value;
          break;
        case 'Rating':
          result.rating = parseFloat(value);
          break;
        case 'Reviews':
          result.reviews = value;
          break;
        case 'Types':
          result.types = value.split(',').map(v => v.trim());
          break;
        case 'Latitude':
          result.latitude = parseFloat(value);
          break;
        case 'Longitude':
          result.longitude = parseFloat(value);
          break;
        default:
          result[key] = value; // fallback
      }
    });
  
    return result;
  }
  

export default {
    state,
    getters,
    actions,
    mutations
}