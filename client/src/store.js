import { createStore } from 'vuex';
import itineraryStore from './modules/itineraryStore';
import createPersistedState from 'vuex-persistedstate';
import Cookies from 'js-cookie';

const store = createStore({
    modules: {
        itineraryStore
    },
    plugins: [createPersistedState({
        getState: (key) => Cookies.get(key),
        setState: (key, state) => Cookies.set(key, state, { expires: 3, secure: true })
    })],
});

export default store 