import React from 'react';
import slidebar1 from "./assets/full_shot_man_carrying_baggage.jpg"
export const Slidebar = () => {
  return (
    <>
     <div>
      {/* Carousel */}
      <div id="default-carousel" className="relative w-full" data-carousel="slide">
        {/* Carousel wrapper */}
        <div className="relative h-56 overflow-hidden rounded-lg md:h-96">
          {/* Example Image 1 */}
          <div className="hidden duration-700 ease-in-out" data-carousel-item>
            <img
              src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg"
              className="absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2"
              alt="Carousel Image 1"
            />
          </div>
          {/* Example Image 2 */}
          <div className="hidden duration-700 ease-in-out" data-carousel-item>
          <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="Trulli" width="500" height="333"/>

          </div>
          {/* ... (Repeat for other items) */}
        </div>
        {/* Slider indicators */}
        <div className="absolute z-30 flex -translate-x-1/2 bottom-5 left-1/2 space-x-3 rtl:space-x-reverse">
          <button
            type="button"
            className="w-3 h-3 rounded-full"
            aria-current="true"
            aria-label="Slide 1"
            data-carousel-slide-to="0"
          ></button>
          {/* ... (Repeat for other indicators) */}
        </div>
        {/* Slider controls */}
        <button
          type="button"
          className="absolute top-0 start-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none"
          data-carousel-prev
        >
          {/* ... (Your existing previous button content) */}
        </button>
        <button
          type="button"
          className="absolute top-0 end-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none"
          data-carousel-next
        >
          {/* ... (Your existing next button content) */}
        </button>
      </div>

      {/* Additional content below the carousel from 80% */}
      <div className="relative w-full h-[20%] bg-white rounded-lg shadow-md flex flex-col p-6 gap-y-4">
        <h2 className="text-xl font-bold"></h2>
        <div className="flex flex-row gap-x-4">
          {/* ... (Rest of your additional content) */}
        </div>
      </div>
    </div>
    </>
  );
};
