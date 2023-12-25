// App.jsx
import React from 'react';
import  {Route, Routes } from 'react-router-dom';
import UserRegisterForm from './components/auth/UserRegisterForm';
const App = () => {
  return (
    <>
    <Routes>
        <Route path="/register" element={<UserRegisterForm/>} />
        {/* <Route path="/" exact element={<Home/>} /> */}

     
    </Routes>
    </>
  );
};

export default App;
