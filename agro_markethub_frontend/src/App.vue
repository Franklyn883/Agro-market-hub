<template>
<header>
    <nav class="navbar">
        <div class="navbar__logo">
            <h1 class="logo">AgroHub</h1>
        </div>
        <ul class="navbar__items">
            <li class="navbar__item">
                <h3>Products</h3>
            </li>
            <li class="navbar__item">
                <h3>Cart</h3>
            </li>
        </ul>
    </nav>
</header>
</template>

<style lang="scss">
*{
    margin:0;
    padding:0;
    box-sizing: border-box;
}
.navbar{
    background-color: #3E8C4B;
    color: #ffffff;
    padding:0.5em;
    display:flex;
    gap:1em;
}
.navbar ul{
    list-style: none;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex: 1;
}
</style>
