import React from "react";
import { cn } from "";

const Card = React.forwardRef(({ className, ...props  }, ref)=>(
  <div
   ref={ref}
   className={cn (
    "rounded-lg border bg-card text-card-foreground shadow-sm ",
    className
   )}
   {...props}

  />

));

Card.displayName ="Card";

const CardHeader = React.forwardRef(( {className, ...props}, ref )=>(
  <div
   ref={ref}
   className={cn("flex flex-col space-y-1.5 p-6", className)}
   {...props}

  />


));

CardHeader.displayName = "CardHeader";

const CardTitle = React.forwardRef(({className, ...props},ref) =>(
  ref={ref}
  className={cn("")}
))