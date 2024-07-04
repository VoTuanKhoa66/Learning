<template>
  <div>
    <header class="py-3 text-white">
      <div class="container">
        <div
          class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start"
        >
          <ul
            class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0"
          >
            <li>
              <NuxtLink to="/" class="nav-link px-0 me-4">
                <img src="../assets/images/logo.png" alt="" />
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="/" class="nav-link px-2 me-4">Home</NuxtLink>
            </li>
            <li>
              <NuxtLink to="/about" class="nav-link px-2 me-4">About</NuxtLink>
            </li>
            <li>
              <NuxtLink to="/movies" class="nav-link px-2 me-4"
                >Movies</NuxtLink
              >
            </li>
          </ul>

          <div class="search-form">
            <font-awesome :icon="['fas', 'magnifying-glass']" class="icon" />
            <div class="search-input">
              <input placeholder="Titles, people, genres" />
            </div>
          </div>
        </div>
      </div>
    </header>

    <!-- output the page content -->
    <div class="content">
      <slot />
    </div>

    <!-- <footer class="py-3 my-4">
      <ul class="nav justify-content-center border-bottom pb-3 mb-3">
        <li class="nav-item">
          <a href="#" class="nav-link px-2 text-muted">Home</a>
        </li>
        <li class="nav-item">
          <a href="#" class="nav-link px-2 text-muted">Features</a>
        </li>
        <li class="nav-item">
          <a href="#" class="nav-link px-2 text-muted">Pricing</a>
        </li>
        <li class="nav-item">
          <a href="#" class="nav-link px-2 text-muted">FAQs</a>
        </li>
        <li class="nav-item">
          <a href="#" class="nav-link px-2 text-muted">About</a>
        </li>
      </ul>
      <p class="text-center text-muted">© 2022 Company, Inc</p>
    </footer> -->
  </div>
</template>
  
<script setup>
import "../assets/styles/global.css";
</script>
  
<style scoped>
.router-link-exact-active {
  color: #fff;
}
.router-link-exact-active:hover {
  color: inherit;
}
a {
  color: grey;
}
a:hover {
  color: grey;
}
header {
  z-index: 2;
  background-color: rgba(0, 0, 0, 1);
  position: fixed;
  width: 100%;
  top: 0;
}
/* .content {
  margin-top: 100px;
} */
.nav-link img {
  width: 92.5px;
  height: 29.6px;
}
.search-form {
  display: flex;
  align-items: center;
}
.icon {
  cursor: pointer;
  margin-right: 10px;
}
.search-form {
  width: 275px;
  padding: 5px 10px;
  border: 1px solid white;
  align-items: center;
  display: flex;
  margin-right: 20px;
}

.search-form .search-input input:focus {
  outline: none;
}

.search-form .search-input input {
  border: none;
  margin-left: 10px;
  color: white;
  background-color: transparent;
  font-size: 14px;
  font-weight: 500;
}
</style>
  