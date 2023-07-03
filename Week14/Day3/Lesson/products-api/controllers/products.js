const { getAllProducts,
        getProduct,
        insertProduct,
        deleteProduct,
        updateProduct,
        searchProducts
} = require('../modules/products.js')

const _getAllProducts = (req, res) => {
  getAllProducts()
  .then(data => {
    res.json(data)
  })
  .catch(err => {
    console.log(err);
    res.status(404).json({msg:'not found'})
  })
}

const _getAllProductsEjs = (req, res) => {
  getAllProducts()
  .then(data => {
    // res.json(data)
    res.render('shop', {products:data} )
  })
  .catch(err => {
    console.log(err);

    res.render("404",{msg:'not found'})
  })
}

const _getProduct = (req,res) => {
  getProduct(req.params.id)
  .then(data => {
    res.json(data)
  })
  .catch(err => {
    console.log(err);
    res.status(404).json({msg:'not found'})
  })
}

// insertProduct
const _insertProduct = (req, res) => {
  insertProduct(req.body)
  .then(data => {
    res.json(data)
  })
  .catch(err => {
    console.log(err);
    res.status(404).json({msg:'not found'})
  })
}

const _deleteProduct = (req, res) => {
  deleteProduct(req.params.id)
  .then(data => {
    res.json(data)
  })
  .catch(err => {
    console.log(err);
    res.status(404).json({msg:'not found'})
  })
}

const _updateProduct = (req,res) => {
  updateProduct(req.params.id, req.body)
  .then(data => {
    res.json(data)
  })
  .catch(err => {
    console.log(err);
    res.status(404).json({msg:'not found'})
  })
}

const _searchProducts = (req,res) =>{
  searchProducts(req.query.name)
  .then(data => {
    res.json(data)
  })
  .catch(err => {
    console.log(err);
    res.status(404).json({msg:'not found'})
  })
}

module.exports = {
  _getAllProducts,
  _getProduct,
  _insertProduct,
  _deleteProduct,
  _updateProduct,
  _searchProducts,
  _getAllProductsEjs
}
