function generateSKU() {
    let category = document.getElementById('category').value;
    let productName = document.getElementById('product_name').value;
    let quantity = document.getElementById('quantity').value;

    if (!productName || !quantity) {
        document.getElementById('sku_output').innerText = "Please fill in all fields.";
        return;
    }

    let sku = category.slice(0, 3).toUpperCase() + "-" + 
              productName.slice(0, 4).toUpperCase() + "-" + 
              quantity;

    document.getElementById('sku_output').innerText = "SKU: " + sku;
}

function createOrder() {
    let checkboxes = document.querySelectorAll('.item');
    let subtotal = 0;

    checkboxes.forEach(box => {
        if (box.checked) {
            subtotal += parseFloat(box.value);
        }
    });

    let tax = subtotal * 0.12;
    let total = subtotal + tax;

    document.getElementById('subtotal').innerText = subtotal.toFixed(2);
    document.getElementById('tax').innerText = tax.toFixed(2);
    document.getElementById('total').innerText = total.toFixed(2);
}

function createOrder() {
  let checkboxes = document.querySelectorAll('.item');
  let subtotal = 0;

  
  checkboxes.forEach(box => {
    if (box.checked) {
      subtotal += parseFloat(box.value);
    }
  });

  let tax = subtotal * 0.12;
  let total = subtotal + tax;


  document.getElementById('subtotal').innerText = subtotal.toFixed(2);
  document.getElementById('tax').innerText = tax.toFixed(2);
  document.getElementById('total').innerText = total.toFixed(2);
}
