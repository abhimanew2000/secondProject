// App.jsx
import React from 'react';
import  {Route, Routes } from 'react-router-dom';
import UserRegisterForm from './components/auth/UserRegisterForm';
import Test from './components/Test';
import UserLoginForm from './components/auth/UserLoginForm';
import AdminLoginForm from './components/auth/AdminLoginForm';
import { AdminHomePage } from './Pages/AdminHomePage';
import HomePage from './Pages/UserHomePage';
import { SearchBar } from './SearchBar';
import HotelList from './Hotellist';
// import { AdminHomePage } from './Pages/AdminHomePage';
const App = () => {
  return (
    <>
    <Routes>
        <Route path="/register" element={<UserRegisterForm/>} />
        <Route path='/test' element={<HotelList/>}/>
        <Route path='/login' element={<UserLoginForm />}/>
        <Route path='/admin/login' element={<AdminLoginForm />}/>
        <Route path="/" element={<HomePage />} />
        <Route path="/admin/dashboard" element={<AdminHomePage/>} />



    </Routes>
    </>
  );
};

export default App;
