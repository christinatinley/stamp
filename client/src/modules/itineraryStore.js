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
    async fetchHome({commit}) {
        try {
            const response = await axios.get('http://127.0.0.1:5000/');
            console.log('Home response:', response.data);
        } catch (error) {
            console.error('Error fetching home data:', error);
        }
    },

    async fetchItinerary({ state }) {
      try {
        const response = await axios.post('/api/itinerary', state.formData);
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

export default {
    state,
    getters,
    actions,
    mutations
}