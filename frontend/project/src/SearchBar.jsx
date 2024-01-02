import React, { useEffect, useState } from "react";
import DatePicker, { DateObject } from "react-multi-date-picker";
import { useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { increment, decrement } from "./redux/slices/roomSelectionSlice";
export const SearchBar = () => {
  const navigate = useNavigate();
  const [checkInDate, setCheckInDate] = useState(null);
  const [checkOutDate, setCheckOutDate] = useState(null);
  const [dates, setDates] = useState([new DateObject(), new DateObject()]);
  const currentDate = new DateObject();

  // -----------search-----
  const [searchValue, setSearchValue] = useState("");
  const [citySuggestions, setCitySuggestions] = useState([]);
  const fetchData = async (value) => {
    try {
      const url = `http://127.0.0.1:8000//api/autocomplete_city/?query=${value}`;
      const response = await fetch(url);

      if (response.ok) {
        const data = await response.json();
        const uniqueCities = [...new Set(data)].slice(0, 5);
        setCitySuggestions(uniqueCities);
      } else {
        console.error("Error fetching city suggestions:", response.statusText);
      }
    } catch (error) {
      console.error("Error fetching city:", error);
    }
  };

  const handleChange = (value) => {
    setSearchValue(value);
    fetchData(value);
  };
  const handleClear = () => {
    setSearchValue("");
    setCitySuggestions([]); // Clear suggestions when the input is cleared
  };

  const handleCitySelect = (selectedCity) => {
    setSearchValue(selectedCity);
    setCitySuggestions([]);
  };

  // ------------------------------------

  useEffect(() => {
    if (dates[0]) {
      setCheckInDate(dates[0].toDate());
    }
    if (dates[1]) {
      setCheckOutDate(dates[1].toDate());
    }
  }, [dates[0], dates[1]]);
  // ------------------------------------------------------------
  const [selectedValues, setSelectedValues] = useState({
    adults: 1,
    children: 0,
    rooms: 1,
  });

  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const toggleDropdown = () => {
    setIsDropdownOpen(!isDropdownOpen);
  };

  const { numAdults, numChildren, numRooms } = useSelector(
    (state) => state.roomSelection
  );
  const dispatch = useDispatch();

  const handleIncrement = (category) => {
    console.log("hiiii");
    dispatch({ ...increment(category) });
  };

  const handleDecrement = (category) => {
    dispatch(decrement(category));
  };

  useEffect(() => {
    setSelectedValues({
      adults: numAdults,
      children: numChildren,
      rooms: numRooms,
    });
  }, [numAdults, numChildren, numRooms]);

  // ----------------------------------------------------------
  return (
    <div className="absolute top-[500px] max-w-[1100px] w-[calc(100%-10px)] left-1/2 transform -translate-x-1/2 -translate-y-54 z-3 h-fit">
      <div className="flex flex-col h-fit">
        <div className="rounded-lg h-fit shadow-md bg-yellow-500 border-yellow-500 border-4">
          <div className="grid grid-cols-7 h-fit items-center">
            <div className="relative col-span-2 ml-2  ">
              <input
                type="text"
                value={searchValue}
                className="pl-8 pr-2  py-2 rounded-md border border-gray-300 focus:outline-none focus:ring focus:border-blue-500 w-full"
                placeholder="Enter the City Name"
                onChange={(e) => handleChange(e.target.value)}
              />
              {citySuggestions.length > 0 && (
                <ul>
                  {searchValue && citySuggestions.length > 0 && (
                    <ul className="absolute bg-white shadow-2xl w-full mt-3 p-5 border border-gray-300 rounded-lg">
                      {citySuggestions.map((city, index) => (
                        <li key={index} onClick={() => handleCitySelect(city)}>
                          {city}
                        </li>
                      ))}
                    </ul>
                  )}
                </ul>
              )}
              {searchValue && (
                <button
                  onClick={handleClear}
                  style={{
                    position: "absolute",
                    right: "5px",
                    top: "50%",
                    transform: "translateY(-50%)",
                    cursor: "pointer",
                    border: "none",
                    background: "none",
                  }}
                >
                  <svg
                    // Assuming you have an SVG icon for the close action
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="currentColor"
                  >
                    <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z" />
                  </svg>
                </button>
              )}
            </div>
            <div className="relative col-span-2 mx-2">
              <div className="grid grid-cols- h-fit">
                <DatePicker
                  inputClass="pl-8 pr-2 py-2 rounded-md border border-gray-300 focus:outline-none focus:ring focus:border-blue-500 w-full"
                  containerClassName="custom_container-picker"
                  value={dates}
                  onChange={setDates}
                  numberOfMonths={2}
                  range
                  rangeHover
                  format="MMMM DD"
                  minDate={currentDate}
                />
              </div>
            </div>
            <div className="relative col-span-2 mr-2">

              <button
                onClick={toggleDropdown}
                style={{
                  position: "absolute",
                  right: "5px",
                  top: "50%",
                  transform: "translateY(-50%)",
                  cursor: "pointer",
                  border: "none",
                  background: "none",
                }}
              >
                <svg
                  // Assuming you have an SVG icon for the dropdown
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="currentColor"
                >
                  <path d="M7 10l5 5 5-5z" />
                </svg>
              </button>
              {isDropdownOpen && (
                <div className="absolute top-full bg-white shadow-2xl mt-3 w-full p-2 border border-gray-300 rounded-lg flex flex-col justify-center">
                  <div className="flex flex-col mx-10">
                    <div className="flex items-center justify-between pt-1 ">
                      <label>Adults:</label>
                      <div className="flex items-center border border-gray-400  rounded-lg py-2">
                        <button
                          className="px-5  text-blue-500"
                          onClick={() => handleIncrement("numAdults")}
                        >
                          +
                        </button>
                        <span>{numAdults}</span>
                        <button
                          className="px-5"
                          onClick={() => handleDecrement("numAdults")}
                        >
                          -
                        </button>
                      </div>
                    </div>
                    <div className="flex items-center justify-between pt-1 ">
                      <label>Children:</label>
                      <div className="flex items-center border border-gray-400  rounded-lg py-2">
                        <button
                          className="px-5  text-blue-500"
                          onClick={() => handleIncrement("numChildren")}
                        >
                          +
                        </button>
                        <span>{numChildren}</span>
                        <button
                          className="px-5"
                          onClick={() => handleDecrement("numChildren")}
                        >
                          -
                        </button>
                      </div>
                    </div>
                    <div className="flex items-center justify-between pt-1 ">
                      <label>Rooms:</label>
                      <div className="flex items-center border border-gray-400  rounded-lg py-2">
                        <button
                          className="px-5 text-blue-500"
                          onClick={() => handleIncrement("numRooms")}
                        >
                          +
                        </button>
                        <span>{numRooms}</span>
                        <button
                          className="px-5"
                          onClick={() => handleDecrement("numRooms")}
                        >
                          -
                        </button>
                      </div>
                    </div>

                    <button className="border-2 rounded-md border-blue-500 my-2 py-2">
                      Done
                    </button>
                  </div>
                </div>
              )}
              <input
              
                className="pl-8 pr-2 py-2 rounded-md bg-white border border-gray-300 focus:outline-none focus:ring focus:border-blue-500 w-full"
                placeholder=""
                disabled
                value={`${numAdults} adults.${numChildren} children. ${numRooms} rooms`}
              />

            </div>
            <button className="col-span-1 bg-blue-500 text-white h-12 rounded-xl  hover:bg-blue-600 focus:outline-none focus:ring focus:border-blue-300 border-yellow-500 border-4">
              {/* Adjusted yellow border */}
              Search
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
