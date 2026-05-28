import React, { useState } from "react";
import { Provider } from "react-redux";
import { store } from "./redux/store.js";
import AboutUs from "./components/AboutUs.jsx";
import ProductList from "./components/ProductList.jsx";
import CartItem from "./components/CartItem.jsx";
import "./App.css";

const LandingPage = ({ onNavigate }) => (
  <section className="landing-page">
    <div className="background-image" aria-hidden="true" />
    <div className="landing-overlay" />
    <div className="landing-content">
      <p className="eyebrow">Indoor plants and calm living</p>
      <h1>Welcome to Paradise Nursery</h1>
      <p>
        Bring home healthy plants that add life, texture, and freshness to your space.
      </p>
      <button className="primary-button" onClick={() => onNavigate("products")}>
        Get Started
      </button>
    </div>
  </section>
);

const AppShell = () => {
  const [view, setView] = useState("home");

  return (
    <>
      {view === "home" && <LandingPage onNavigate={setView} />}
      {view === "about" && <AboutUs onNavigate={setView} />}
      {view === "products" && <ProductList currentView={view} onNavigate={setView} />}
      {view === "cart" && <CartItem currentView={view} onNavigate={setView} />}
    </>
  );
};

const App = () => (
  <Provider store={store}>
    <AppShell />
  </Provider>
);

export default App;
