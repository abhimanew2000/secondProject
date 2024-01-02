// src/components/HotelList.jsx

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const HotelList = () => {
    const [hotels, setHotels] = useState([]);

    useEffect(() => {
        // Fetch hotels from the API
        axios.get('http://127.0.0.1:8000/api/hotels/')
            .then(response => {
                setHotels(response.data);
            })
            .catch(error => {
                console.error('Error fetching hotels:', error);
            });
    }, []);

    return (
        <div className="container mx-auto mt-8">
            <h2 className="text-2xl font-bold mb-4">Hotel List</h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                {hotels.map(hotel => (
                    <div key={hotel.id} className="bg-white p-4 rounded-md shadow-md">
                        <img src={hotel.image} alt={hotel.name} className="w-full h-32 object-cover mb-4 rounded-md" />
                        <h3 className="text-lg font-semibold mb-2">{hotel.name}</h3>
                        <p className="text-gray-600">{hotel.city}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default HotelList;
