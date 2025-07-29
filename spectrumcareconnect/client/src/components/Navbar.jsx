// src/components/Navbar.jsx
import { useState } from "react";
import { Menu, X } from "lucide-react";
import logo1 from "../assets/logo.png";
import { Activity, BookOpen, Calendar, Gamepad2, User2, Users, GraduationCap } from "lucide-react";

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const navLinks = ["Autism", "Awareness Hub", "Therapy & Booking", "Games & Learning", "Parent Support", "Community","School Integration",];
  const navIcons = [{ name: "Autism", Icon: Activity },{ name: "Awareness Hub", Icon: BookOpen },{ name: "Therapy & Booking", Icon: Calendar }, { name: "Games & Learning", Icon: Gamepad2 }, { name: "Parent Support", Icon: User2 },{ name: "Community", Icon: Users }, { name: "School Integration", Icon: GraduationCap },];

  return (
    <nav className="bg-white shadow-md fixed top-0 left-0 right-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between">
        {/* Logo + Brand Name */}
        <div className="flex items-center space-x-3">
          <img src={logo1} alt="Logo" className="h-25 w-auto" />



          <span className="text-xl sm:text-2xl font-bold text-purple-600">
            {/*sectrumCareConnect*/}
          </span>
        </div>

        {/* Desktop Navigation */}
        <div className="hidden md:flex space-x-6">
           {navIcons.map(({ name, Icon }, idx) => (
              <a
                key={idx}
                href="#"
                className="flex items-center space-x-2 text-gray-700 hover:text-purple-600 transition-colors duration-200 text-sm sm:text-base"
              >
                <Icon size={18} />
                <span>{name}</span>
              </a>
            ))}

        </div>

        {/* Mobile Toggle Button */}
        <div className="md:hidden">
          <button
            onClick={() => setIsOpen(!isOpen)}
            className="text-gray-700 hover:text-purple-600"
          >
            {isOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>
      </div>

      {/* Mobile Dropdown */}
      {isOpen && (
        <div className="md:hidden bg-white px-4 pb-4 space-y-2">
          {navIcons.map(({ name, Icon }, idx) => (
              <a
                key={idx}
                href="#"
                className="flex items-center space-x-2 text-gray-700 hover:text-purple-600 transition-colors text-base"
              >
                <Icon size={18} />
                <span>{name}</span>
              </a>
            ))}

        
        </div>
      )}
    </nav>
  );
};

export default Navbar;
