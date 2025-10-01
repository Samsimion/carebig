import React, {useState} from "react"
import Navbar from "../components/Navbar";
import HeroSection from "../components/HeroSection";
import FeatureCategories from "../components/FeatureCategories";





function Landingpage (){
    return (
        <>
            <div className="min-h-screen bg-gray-50">
                <Navbar />
                    <div className="pt-24 px-4">
                        <h1 className="text-3xl font-bold text-center text-purple-600">Welcome to SpectrumCareConnect</h1>
                        
                    </div>
                <HeroSection />
                
            </div>

            <FeatureCategories/>
           
        </>
    )

}export default Landingpage



