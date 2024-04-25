import React, { useState } from "react";
import SearchBar from "./SearchBar"
import ProductTable from "./ProductTable"

function FilterableProductTable({ products }) {
  const [search, setSearch] = useState("")
  const [showInStock, setShowInStock] = useState(false)
  
  return (
    <div>
      <SearchBar 
        search={search} 
        showInStock={showInStock} 
        onSearchChange={setSearch} 
        onShowStockChange={setShowInStock} 
      />
      <ProductTable products={products} search={search} showInStock={showInStock} />
    </div>
  )
}

export default FilterableProductTable