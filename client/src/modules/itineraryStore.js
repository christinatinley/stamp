const state = {
    formData: {
        destination: '',
        startDate: '',
        endDate: '',
        budget: '',
        selectedDates: [],
        blockedTimes: {},
        numberOfTravelers: '',
        lodging: '',
        cuisine: [],
        dietaryRestrictions: [],
      },
}   

const getters = {
    formData: (state) => state.formData,
}

const actions = {
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
    setSelectedDates({ commit }, selectedDates) {
      commit('updateSelectedDates', selectedDates);
    },
    setBlockedTimes({ commit }, blockedTimes) {
      commit('updateBlockedTimes', blockedTimes);
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
    setDietaryRestrictions({ commit }, dietaryRestrictions) {
      commit('updateDietaryRestrictions', dietaryRestrictions);
    },
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
    updateSelectedDates(state, selectedDates) {
        state.formData.selectedDates = selectedDates;
        console.log('Selected dates updated:', selectedDates);
    },
    updateBlockedTimes(state, blockedTimes) {
        state.formData.blockedTimes = blockedTimes;
        console.log('Blocked times updated:', blockedTimes);
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
        state.formData.cuisine = cuisine;
        console.log('Cuisine updated:', cuisine);
    },
    updateDietaryRestrictions(state, dietaryRestrictions) {
        state.formData.dietaryRestrictions = dietaryRestrictions;
        console.log('Dietary restrictions updated:', dietaryRestrictions);
    },
}

export default {
    state,
    getters,
    actions,
    mutations
}