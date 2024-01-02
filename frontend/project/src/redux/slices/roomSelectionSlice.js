// roomSelectionSlice.js
import { createSlice } from '@reduxjs/toolkit';

const roomSelectionSlice = createSlice({
  name: 'roomSelection',
  initialState: {
    numAdults: 1,
    numChildren: 0,
    numRooms: 1,
  },
  reducers: {
    increment: (state, action) => {
      const category = action.payload;
      state[category] += 1;
    },
    decrement: (state, action) => {
      const category = action.payload;

      if (category === "numAdults" && state[category] > 1) {
        state[category] -= 1;
      }

      if (category === "numChildren" && state[category] > 0) {
        state[category] -= 1;
      }

      if (category === "numRooms" && state[category] > 1) {
        state[category] -= 1;
      }
    },
  },
});

export const { increment, decrement } = roomSelectionSlice.actions;

export default roomSelectionSlice.reducer;
