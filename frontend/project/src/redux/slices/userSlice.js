// userSlice.js
import { createSlice } from '@reduxjs/toolkit';

export const userSlice = createSlice({
  name: 'user',
  initialState: {
    name: null,
  },
  reducers: {
    setUserName: (state, action) => {
      state.name = action.payload;
    },
  },
});

export const { setUserName } = userSlice.actions;

export const selectUserName = (state) => state.user.name;

export default userSlice.reducer;
