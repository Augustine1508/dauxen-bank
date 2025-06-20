const toggleBtn = document.getElementById("toggleBalance");
const balance = document.getElementById("balance");
const realBalance = balance.innerHTML;
let visible = true;

toggleBtn.onclick = () => {
    visible = !visible;
    balance.innerHTML = visible ? realBalance : "*******";
    toggleBtn.classList.toggle("fa-eye");
    toggleBtn.classList.toggle("fa-eye-slash");
};
