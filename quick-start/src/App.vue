<script setup>
import MyHeader from "./components/MyHeader.vue";
import "../src/assets/styles/global.css";
import MyCarousel from "./components/MyCarousel.vue";
</script>

<template>
  <MyHeader />
  <div class="container">
    <img
      src="https://m.media-amazon.com/images/M/MV5BODAwM2Q4YTMtYjc0ZC00NjcwLWIwMTAtZDkwYzI3Y2ZlYWI3XkEyXkFqcGc@._V1_.jpg"
      alt=""
    />
    <div class="content">
      <h1>UNDER PARIS</h1>
      <p>
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Repudiandae
        amet mollitia quos laudantium libero animi optio totam est debitis ea
        quam maiores, fuga cum aut numquam saepe vitae reiciendis et!
      </p>
      <div class="buttons">
        <button type="button" class="btn btn-light play-button">
          <font-awesome-icon icon="play" class="icon" />
          <span>Play</span>
        </button>
        <button type="button" class="btn btn-secondary infor-button">
          <font-awesome-icon icon="circle-info" />
          <span>More Infor</span>
        </button>
      </div>
    </div>
    <MyCarousel />
    <div class="block"></div>
  </div>
</template>

<style scoped>
.block{
  height: 200px;
}

.container {
  padding: 0;
  margin: 0;
  max-width: 100%;
}

.thumbnail {
  z-index: 0;
  height: auto;
  max-width: 100%;
  width: 100%;
}
.content {
  z-index: 1;
  color: white;
  position: absolute;
  top: 0;
  padding-left: 170px;
  padding-top: 20%;
  width: 100%;
}

p {
  margin-top: 20px;
  width: 500px;
}

h1 {
  font-size: 70px;
}

.buttons {
  margin-top: 20px;
  display: flex;
}

.play-button span,
.infor-button span {
  margin-left: 10px;
}

.play-button {
  align-items: center;
  width: 130px;
  margin-right: 10px;
  padding: 10px;
  font-size: 18px;
  font-weight: 600;
}

.infor-button {
  align-items: center;
  width: 170px;
  margin-right: 10px;
  padding: 10px;
  font-size: 18px;
  font-weight: 600;
}

.icon {
  width: 22px !important;
  height: 22px !important;
}


</style>
