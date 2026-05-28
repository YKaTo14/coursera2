import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { removeItem, updateQuantity } from "../redux/CartSlice.jsx";
import Navbar from "./Navbar.jsx";

const CartItem = ({ currentView, onNavigate }) => {
  const dispatch = useDispatch();
  const cartItems = useSelector((state) => state.cart.items);
  const cartCount = cartItems.reduce((total, item) => total + item.quantity, 0);
  const calculateTotalAmount = () =>
    cartItems.reduce((total, item) => total + item.price * item.quantity, 0);
  const cartTotal = calculateTotalAmount();

  const handleCheckout = () => {
    window.alert("Coming Soon");
  };

  return (
    <div className="page-shell">
      <Navbar cartCount={cartCount} currentView={currentView} onNavigate={onNavigate} />

      <main className="catalog cart-page">
        <div className="catalog-header">
          <p className="eyebrow">Your shopping cart</p>
          <h2>Review the plants you selected</h2>
        </div>

        {cartItems.length === 0 ? (
          <section className="content-card empty-state cart-item-container">
            <h3>Your cart is empty</h3>
            <p>Browse the plant catalog and add a few favorites.</p>
            <button className="primary-button" onClick={() => onNavigate("products")}>
              Continue Shopping
            </button>
          </section>
        ) : (
          <>
            <div className="cart-list">
              {cartItems.map((item) => {
                const total = item.price * item.quantity;

                return (
                  <article key={item.id} className="cart-row cart-item-container">
                    <img src={item.thumbnail} alt={item.name} />
                    <div className="cart-row-main">
                      <div className="cart-row-top">
                        <div>
                          <h3>{item.name}</h3>
                          <p>Unit price: ${item.price}</p>
                        </div>
                        <strong>${total}</strong>
                      </div>

                      <div className="quantity-controls">
                        <button
                          onClick={() => dispatch(updateQuantity({ id: item.id, delta: -1 }))}
                        >
                          -
                        </button>
                        <span>{item.quantity}</span>
                        <button
                          onClick={() => dispatch(updateQuantity({ id: item.id, delta: 1 }))}
                        >
                          +
                        </button>
                        <button className="delete-button" onClick={() => dispatch(removeItem(item.id))}>
                          Delete
                        </button>
                      </div>
                    </div>
                  </article>
                );
              })}
            </div>

            <aside className="checkout-card">
              <h3>Order Summary</h3>
              <p>Total items: {cartCount}</p>
              <p className="grand-total">Total amount: ${cartTotal}</p>
              <div className="actions">
                <button className="primary-button" onClick={handleCheckout}>
                  Checkout
                </button>
                <button className="secondary-button" onClick={() => onNavigate("products")}>
                  Continue Shopping
                </button>
              </div>
            </aside>
          </>
        )}
      </main>
    </div>
  );
};

export default CartItem;
