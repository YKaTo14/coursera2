import React from "react";

const AboutUs = ({ onNavigate }) => {
  return (
    <section className="about-page">
      <div className="about-us-container content-card about-card">
        <p className="eyebrow">About Paradise Nursery</p>
        <h2>We bring calm, color, and fresh air into everyday spaces.</h2>
        <p>
          Paradise Nursery is a boutique indoor plant shop focused on easy-care
          greenery, thoughtful styling, and healthy plants that feel at home in
          apartments, offices, and cozy homes.
        </p>
        <div className="about-grid">
          <article>
            <h3>Our Mission</h3>
            <p>Help people build a greener space with plants they can keep thriving.</p>
          </article>
          <article>
            <h3>Our Plants</h3>
            <p>We curate succulents, tropical plants, and airy desk-friendly favorites.</p>
          </article>
          <article>
            <h3>Our Care</h3>
            <p>Every order is prepared to arrive ready for a strong and healthy start.</p>
          </article>
        </div>
        <div className="actions">
          <button className="primary-button" onClick={() => onNavigate("products")}>
            Start Shopping
          </button>
          <button className="secondary-button" onClick={() => onNavigate("home")}>
            Back to Home
          </button>
        </div>
      </div>
    </section>
  );
};

export default AboutUs;
