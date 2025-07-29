import React, {useState} from "react";
import heroImage from "../assets/hero.png";

const HeroSection = () => {
  return (
    <section className="bg-gradient-to-br from-blue-100 via-white to-pink-100 py-16 px-4 md:px-8 lg:px-24">
      <div className="flex flex-col-reverse lg:flex-row items-center justify-between max-w-7xl mx-auto">
        
        {/* Left Side: Text */}
        <div className="text-center lg:text-left space-y-6 max-w-xl">
          <h1 className="text-4xl md:text-5xl font-bold text-blue-800 leading-tight">
            Empowering Every Child’s Potential
          </h1>
          <p className="text-lg text-gray-700">
            Helping parents, educators, and doctors support children on the autism spectrum with care, tools, and community.
          </p>
          <button className="px-6 py-3 bg-blue-600 text-white rounded-2xl shadow hover:bg-blue-700 transition">
            Get Started
          </button>
        </div>

        {/* Right Side: Illustration */}
        <div className="mb-10 lg:mb-0 w-full max-w-md lg:max-w-lg">
          <img
            src={heroImage}
            alt="Therapy support illustration"
            className="w-full"
          />
        </div>
      </div>
    </section>
  );
};

export default HeroSection;
