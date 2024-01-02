// store.js
import { configureStore } from '@reduxjs/toolkit';
import userReducer from './slices/userSlice';
import roomSelectionReducer from './slices/roomSelectionSlice'
export const store = configureStore({
  reducer: {
    user: userReducer,
    roomSelection: roomSelectionReducer,


    // other reducers...
  },
});
