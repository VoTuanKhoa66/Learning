<script setup>
import { ref } from "vue";

const links = ref([
  { name: "Home", isCurrent: true },
  { name: "TV Show", isCurrent: false },
  { name: "Movies", isCurrent: false },
  { name: "New & Popular", isCurrent: false },
  { name: "My list", isCurrent: false },
  { name: "Browse by Languages", isCurrent: false },
]);

// const movies = ref([
//   {name: "",image: ""},

// ])

const isActive = ref(false)

function toggleClass(index) {
  links.value.forEach((link, i) => {
    link.isCurrent = i === index;
  });
}

function changeDrodownToggle(){
  isActive.value = !isActive.value
  console.log(isActive.value)
}
</script>

<template>
  <header class="p-3 text-white">
    <div class="container">
      <div
        class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start"
      >
        <a
          href="/"
          class="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none"
        >
          <svg
            class="bi me-2"
            width="40"
            height="32"
            role="img"
            aria-label="Bootstrap"
          >
            <use xlink:href="#bootstrap"></use>
          </svg>
        </a>

        <ul
          class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0"
        >
          <li>
            <a href="#" class="nav-link px-2 me-4"
              ><img src="../assets/images/logo.png" alt=""
            /></a>
          </li>
          <li v-for="(link, index) in links" :key="index">
            <a
              href="#"
              class="nav-link px-2"
              :class="{
                'current-active': link.isCurrent,
                active: !link.isCurrent,
              }"
              @click="toggleClass(index)"
              >{{ link.name }}</a
            >
          </li>
        </ul>

        <div class="search-form">
          <font-awesome-icon icon="magnifying-glass" class="icon"/>
          <div class="search-input">
            <input
            placeholder="Titles, people, genres"
          />
          </div>
        </div>

        <div :class="{'dropup':isActive, 'dropown':!isActive}">
          <a
            @click="changeDrodownToggle"
            href="#"
            class="d-block link-light text-decoration-none dropdown-toggle"
            id="dropdownUser1"
            data-bs-toggle="dropdown"
            aria-expanded="true"
          >
            <img
              src="https://github.com/mdo.png"
              alt="mdo"
              width="32"
              height="32"
              class="rounded-circle"
            />
          </a>
          <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
            <li>
              <div class="item">
                <font-awesome-icon icon="pen" class="icon"/>
                <a class="dropdown-item" href="#">Manage Profiles</a>
              </div>
            </li>
            <li>
              <div class="item">
                <font-awesome-icon icon="address-card" class="icon"/>
                <a class="dropdown-item" href="#">Transfer Profile</a>
              </div>
            </li>
            <li>
              <div class="item">
                <font-awesome-icon icon="user" class="icon"/>
                <a class="dropdown-item" href="#">Account</a>
              </div>
            </li>
            <li>
              <div class="item">
                <font-awesome-icon icon="circle-info" class="icon"/>
                <a class="dropdown-item" href="#">Help Center</a>
              </div>
            </li>
            <li><hr class="dropdown-divider" /></li>
            <li><a class="dropdown-item sign-out" href="#">Sign out of Netflix</a></li>
          </ul>
        </div>
      </div>
    </div>
  </header>
</template>

<style scoped>
header{
  z-index: 5;
  background-color: rgba(0, 0, 0, 0.8);
  position: fixed;
  width: 100%;
}

.nav-link img {
  width: 92.5px;
  height: 29.6px;
}
.nav-link.current-active {
  color: #fff !important;
}
.nav-link.active {
  color: grey !important;
}
.dropdown-menu{
  background: rgba(0, 0, 0, .9);
  padding: 10px;
  margin-top: 60px !important;
  transform: translateX(10px) !important;
}

.dropdown-menu .icon{
  color: #fff;
  width:  22px !important;
  height: 22px !important;
}

.item{
  text-align: start;
  padding: 5px 10px 0 10px;
  align-items: center;
  font-size: 15px;
  font-weight: 500;
  display: flex;
}

.dropdown-item{
  color: #fff;
}

.dropdown-item:hover{
  background: none;
  color: #fff;
  text-decoration: underline;
}

.dropdown-item.sign-out{
  font-size: 15px;
  font-weight: 500;
  padding: 5px 0;
  text-align: center;
}
.dropdown-divider{
  border: #ffffff71 solid 1px;
  margin-top: 10px;
}

.search-form{
  width: 275px;
  padding: 5px 10px;
  border: 1px solid white;
  align-items: center;
  display: flex;
  margin-right: 20px;
}

.search-form .search-input input:focus{
  outline: none;
}


.search-form .search-input input{
  border: none;
  margin-left: 10px;
  color: white;
  background-color: transparent;
  font-size: 14px;
  font-weight: 500;
}

</style>