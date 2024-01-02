// HomePage.jsx
import React from "react";
import { UserNavbar } from "../UserNavbar";
import { SearchBar } from "../SearchBar";

const HomePage = () => {
  return (
    <div>
      <UserNavbar />
      
      
      <img
      
        src="https://r-xx.bstatic.com/xdata/images/xphoto/2880x868/296661902.jpeg?k=81d5ab638f6a52308efde9aff4e7f4d468ee89a8db0677723edf0ff76410d6ec&o="
        alt=""
      />
      <div className="absolute inset-0 px-20 my-32 flex items-center justify-left">

        <div  >
        <h1 className="text-white  text-left font-bold text-5xl mb-4">Wanderlust days <br />and cozy nights</h1>
        <h2 className="text-white text-left font-semibold text-2xl">Choose from cabins, houses, and more

</h2>
<button className="col-span-1 bg-blue-500 text-white h-12 rounded-xl  px-5 hover:bg-blue-600 focus:outline-none focus:ring ">
              {/* Adjusted yellow border */}
              Search
            </button>

        </div>
      </div>
      <SearchBar/>
      

    </div>
  );
};

export default HomePage;
