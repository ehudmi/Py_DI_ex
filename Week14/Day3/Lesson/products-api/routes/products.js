const express = require('express');
const router = express.Router();

const {_getAllProducts,
      _getProduct,
      _insertProduct,
      _deleteProduct,
      _updateProduct,
      _searchProducts,
      _getAllProductsEjs
} = require('../controllers/products.js');
//CRUD
// READ
router.get('/api/products', _getAllProducts);
router.get('/api/products/:id', _getProduct);
router.get('/api/search', _searchProducts);

// CREATE
router.post('/api/products', _insertProduct);
//UPDATE
router.put('/api/products/:id', _updateProduct);
//DELETE
router.delete('/api/products/:id', _deleteProduct);

router.get('/ejs/products', _getAllProductsEjs)

module.exports = {
  router
}
