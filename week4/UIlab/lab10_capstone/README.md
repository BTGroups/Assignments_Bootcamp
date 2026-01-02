# Lab Level 10 – Capstone Submission

## Framework Chosen
- **Tailwind CSS** (v3)  
- Rationale: Mobile-first, utility-first, responsive utilities, easy dark mode support.

## Responsive Strategy
- **Mobile-first design**: Single column layout on small screens.  
- **Responsive grid**:
  - Dashboard/Labs Tracker: `grid-cols-1 md:grid-cols-2`
  - Gallery: `grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4`
- **Utilities used**:
  - `sm:`, `md:`, `lg:`, `xl:` for layout and spacing  
  - `w-full`, `h-full`, `object-cover` for media responsiveness  
- Collapsible modules use `<details>` for JS-free expand/collapse.

## Dark Mode
- Implemented via Tailwind `dark:` variants.  
- Toggle can be activated by adding/removing the `dark` class on `<html>`.

## UX & Polish
- Hover and focus states for buttons, links, images.  
- Smooth transitions using `transition-all` and `duration-300`.  
- Sticky header for navigation.  

## Browser Testing Results
Tested on:
- **Chrome (latest)** – ✅ Fully functional, responsive.  
- **Firefox (latest)** – ✅ Fully functional, responsive.  
- **Safari (latest)** – ✅ Minor scrollbar differences, layout consistent.  
- **Edge (latest)** – ✅ Fully functional, responsive.  

## Folder Structure
