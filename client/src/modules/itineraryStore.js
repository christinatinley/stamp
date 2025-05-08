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
}   

const getters = {
    formData: (state) => state.formData,
}

const actions = {
    async fetchHome() {
        try {
            const response = await axios.get('http://127.0.0.1:5000/');
            console.log('Home response:', response.data);
        } catch (error) {
            console.error('Error fetching home data:', error);
        }
    },

    async fetchItinerary({state}) {
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
                console.log('Times:', times);
                const start = formatDateTime(times.start);
                const end = formatDateTime(times.end);  
                return `${start} - ${end}`;
            })
        }

        console.log('Persona data:', personaData);
        const response = await axios.post('http://127.0.0.1:5000/itinerary', {
            city_name: state.formData.destination,
            persona: personaData,
        });
        console.log('Itinerary response:', response.data);
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
        console.log('Destination updated:', destination);
    },
    updateStartDate(state, startDate) {
        state.formData.startDate = startDate;
        console.log('Start date updated:', startDate);
    },
    updateEndDate(state, endDate) {
        state.formData.endDate = endDate;
        console.log('End date updated:', endDate);
    },
    updateBudget(state, budget) {
        state.formData.budget = budget;
        console.log('Budget updated:', budget);
    },
    updateBlockedTimes(state, { date, times }) {
        state.formData.blockedTimes = {
          ...state.formData.blockedTimes,
          [date]: times,
        };
        console.log('Blocked times updated:', state.formData.blockedTimes);
    },
    updateNumberOfTravelers(state, numberOfTravelers) {
        state.formData.numberOfTravelers = numberOfTravelers;
        console.log('Number of travelers updated:', numberOfTravelers);
    },
    updateLodging(state, lodging) {
        state.formData.lodging = lodging;
        console.log('Lodging updated:', lodging);
    },
    updateCuisine(state, cuisine) {
        console.log('Cuisine:', cuisine);
        state.formData.cuisines = cuisine;
        console.log('Blocked times updated:', state.formData.cuisine);
    },
    updateDietaryRestrictions(state, dietaryRestriction) {
        console.log('Dietary restrictions:', dietaryRestriction);
        state.formData.dietaryRestrictions = dietaryRestriction;
        console.log('Dietary restrictions updated:', state.formData.dietaryRestrictions);
    },
    updateExperiences(state, {experience, rating}) {
        state.formData.experiences = {
            ...state.formData.experiences,
            [experience]: rating,
        };
    }
}

function formatDateTime(date) {
    console.log('Date:', date);
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

export default {
    state,
    getters,
    actions,
    mutations
}