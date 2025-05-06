import { createStore } from 'vuex';
import itineraryStore from './modules/itineraryStore';

const store = createStore({
    modules: {
        itineraryStore
    }
});

export default store 