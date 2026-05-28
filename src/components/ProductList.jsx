import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { addItem } from "../redux/CartSlice.jsx";
import { plantCatalog, plantCategories } from "../data/plants.js";
import Navbar from "./Navbar.jsx";

const ProductList = ({ currentView, onNavigate }) => {
  const dispatch = useDispatch();
  const cartItems = useSelector((state) => state.cart.items);
  const cartCount = cartItems.reduce((total, item) => total + item.quantity, 0);
  const cartIds = new Set(cartItems.map((item) => item.id));

  const groupedPlants = plantCategories.map((category) => ({
    category,
    plants: plantCatalog.filter((plant) => plant.category === category),
  }));

  return (
    <div className="page-shell">
      <Navbar cartCount={cartCount} currentView={currentView} onNavigate={onNavigate} />

      <main className="catalog">
        <div className="catalog-header">
          <p className="eyebrow">Choose your plants</p>
          <h2>Fresh picks for every room</h2>
          <p>
            Browse our curated collection by category. Add what you love, then
            move straight to the cart to review your order.
          </p>
        </div>

        {groupedPlants.map(({ category, plants }) => (
          <section key={category} className="category-block">
            <h3>{category}</h3>
            <div className="product-grid">
              {plants.map((plant) => {
                const inCart = cartIds.has(plant.id);

                return (
                  <article key={plant.id} className="product-card">
                    <img src={plant.thumbnail} alt={plant.name} />
                    <div className="product-body">
                      <div className="product-meta">
                        <h4>{plant.name}</h4>
                        <span>${plant.price}</span>
                      </div>
                      <p>Healthy, easy-care plant for brightening your space.</p>
                      <button
                        className="primary-button"
                        disabled={inCart}
                        onClick={() => dispatch(addItem(plant))}
                      >
                        {inCart ? "Added to Cart" : "Add to Cart"}
                      </button>
                    </div>
                  </article>
                );
              })}
            </div>
          </section>
        ))}
      </main>
    </div>
  );
};

export default ProductList;
