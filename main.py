from pyscript import document, display


def generate_order():
    # Get user info
    name = document.getElementById("custName").value
    address = document.getElementById("custAddress").value
    contact = document.getElementById("custContact").value

    # Get checkboxes
    p1 = document.getElementById("p1")
    p2 = document.getElementById("p2")
    p3 = document.getElementById("p3")
    p4 = document.getElementById("p4")
    p5 = document.getElementById("p5")

    # Compute total
    total = (
        4400 * int(p1.checked) +
        5500 * int(p2.checked) +
        5600 * int(p3.checked) +
        5500 * int(p4.checked) +
        3000 * int(p5.checked)
    )

    # Selected products
    chosen = (
        "Mikasa V300W - ₱4400<br>" * int(p1.checked) +
        "Molten V5M5000 - ₱5500<br>" * int(p2.checked) +
        "Mikasa V200W - ₱5600<br>" * int(p3.checked) +
        "Mikasa BV550C - ₱5500<br>" * int(p4.checked) +
        "Wilson OPTX AVP - ₱3000<br>" * int(p5.checked)
    )

    # If no item chosen
    if chosen == "":
        chosen = "No products selected.<br>"

    # Create summary
    summary = "<h3>Order Summary</h3>"
    summary += "<p><b>Name:</b> " + name + "<br>"
    summary += "<b>Address:</b> " + address + "<br>"
    summary += "<b>Contact:</b> " + contact + "</p>"
    summary += "<p><b>Items Ordered:</b><br>" + chosen + "</p>"
    summary += "<p><b>Total:</b> ₱" + str(total) + "</p>"
    summary += "<p>✅ Thank you for your order!</p>"

    # Display output
    document.getElementById("output").innerHTML = summary
