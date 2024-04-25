import React from "react";

function SearchBar({ search, showInStock, onSearchChange, onShowStockChange }) {
  return (
    <form style={{ padding: "10px", display: "flex", flexDirection: "column" }}>
      <input 
        type="text" 
        placeholder="Search..." 
        value={search} 
        onChange={e => onSearchChange(e.target.value)} 
      />
      <label>
        <input 
          type="checkbox" 
          checked={showInStock} 
          onChange={e => onShowStockChange(e.target.checked)} 
        />
        Only show products in stock
      </label>
    </form>
  )
}

export default SearchBar