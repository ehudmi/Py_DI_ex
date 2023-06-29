const {db} = require('../config/dbsql.js');

const getAllProducts = () => {
  // return db.raw('select id, name, price from products')
  return db('products')
  .select('id','name','price')
  .orderBy('name')
}

const getProduct = (id) => {
  return db('products')
  .select('id','name','price')
  .where({id})
}

// insert - name, price
const insertProduct = (product) => {
  return db('products')
  .insert(product) // {name:'...', price: '...'}
  .returning('*')
}

// delete - one product by idea
const deleteProduct = (id) => {
  return db('products')
  .where({id})
  .del()
  .returning('*')
}

// update product by id - params, name & price - body
const updateProduct = (id, product) => {
  return db('products')
  .update(product) // {naem:..., price:...}
  .where({id})
  .returning('*')
}

const searchProducts = (name) => {
  return db('products')
  .select('id','name','price')
  .whereILike('name', `${name}%` )
}

module.exports = {
  getAllProducts,
  getProduct,
  insertProduct,
  deleteProduct,
  updateProduct,
  searchProducts
}
