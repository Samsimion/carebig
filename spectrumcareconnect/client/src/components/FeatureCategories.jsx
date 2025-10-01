import {BookOpen , Calendar, GamepadIcon, GraduationCap, Users,Sparkles, Badge as BadgeIcon} from 'lucide-react'
// import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
 import { Badge } from './ui/Badge';

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "./ui/Card";


function FeatureCategories(){
    const categories = [
        {
            icon:BookOpen,
            title:"Awareness & Education",
            description: "Comprehensive spectrum information, diagnosis guides, and educational resources",
            features:["Autism Types & Info", "Symptom Checker", "Therapy Types Guide", "Awareness Campaigns"],
            count:"6 Features",
            gradient:"bg-gradient-primary",
        },
        {
            icon: Calendar,
            title: "Therapy & Booking",
            description:"Connect with therapists, book sessions, and track progress securely",
            features: ["Book Therapist Sessions", "Virtual Therapy", "Progress Tracking", "Medical Records"],
            count: "5 Features",
            gradient: "bg-gradient-secondary",
        },
        {
            icon:GamepadIcon,
            title:"Games & Learning",
            description: "Interactive, child-friendly educational games and activities",
            features: ["Educational Games", "Sensory Tools", "Social Simulations", "Achievement System"],
            count: "5 Features",
            gradient: "bg-gradient-warm"
        },
        {
            icon:Users,
            title: "Parent Support",
            description: "Forums, expert Q&As, and mental wellness resources for families",
            features: ["Parent Forums", "Expert Q&As", "Parenting Tips", "Mental Wellness"],
            count:"7 Features",
            gradient: "bg-gradient-primary"
        },
        {
            icon:GraduationCap,
            title: "Personalization",
            description: "Adaptive features, custom themes, and AI-powered recommendations",
            features: ["Custom Themes", "AI Recommendations", "Language Options", "Offline Mode"],
            count: "6 Features",
            gradient:"bg-gradient-warm"
        },
        {
            icon: Sparkles,
            title: "Tech & Insights",
            description: "Advanced analytics, secure profiles, and administrative tools",
            features: ["AI Recommendations", "Insights Dashboard", "Secure Profiles", "In-App Store"],
            count: "5 Features",
            gradient: "bg-gradient-primary"
        }
    ];

    return (
        <section id="features" className="bg-gradient-to-br from-blue-100 via-white to-pink-100  px-4 md:px-8 lg:px-24 py-20 bg-muted/30">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <Badge variant="secondary" className="mb-4">
            Comprehensive Platform
          </Badge>
          <h2 className="text-3xl lg:text-5xl font-bold text-foreground mb-6">
            Everything Your Family Needs
          </h2>
          <p className="text-lg text-muted-foreground max-w-3xl mx-auto">
            From awareness and therapy to games and community support - discover all 38 features 
            organized into 7 comprehensive categories designed for autism families.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {categories.map((category, index) => (
            <Card 
              key={index}
              className="group hover:shadow-medium transition-all duration-300 hover:scale-105 cursor-pointer border-2 hover:border-primary/20"
            >
              <CardHeader className="pb-4">
                <div className="flex items-center justify-between mb-4">
                  <div className={`p-3 rounded-xl ${category.gradient} shadow-soft`}>
                    <category.icon className="w-6 h-6 text-white" />
                  </div>
                  <Badge variant="outline" className="text-xs">
                    {category.count}
                  </Badge>
                </div>
                <CardTitle className="text-xl group-hover:text-primary transition-colors">
                  {category.title}
                </CardTitle>
                <CardDescription className="text-muted-foreground">
                  {category.description}
                </CardDescription>
              </CardHeader>
              
              <CardContent>
                <ul className="space-y-2">
                  {category.features.map((feature, featureIndex) => (
                    <li key={featureIndex} className="flex items-center text-sm text-muted-foreground">
                      <div className="w-1.5 h-1.5 bg-primary rounded-full mr-3 flex-shrink-0"></div>
                      {feature}
                    </li>
                  ))}
                </ul>
              </CardContent>
            </Card>
          ))}
        </div>

        {/* Trust indicators */}
        {/* <div className="mt-16 text-center">
          <div className="flex items-center justify-center space-x-2 text-muted-foreground mb-4">
            <Shield className="w-5 h-5" />
            <span className="text-sm font-medium">Secure, Private, and HIPAA-Compliant</span>
          </div>
          <p className="text-sm text-muted-foreground max-w-2xl mx-auto">
            Built with privacy and security at its core. All medical data is encrypted and stored securely, 
            giving families complete control over their information.
          </p>
        </div> */}
      </div>
    </section>
    )



}export default FeatureCategories