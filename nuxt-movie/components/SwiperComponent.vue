<template>
  <Swiper
    :slides-per-view="5"
    :loop="true"
    :effect="'creative'"
    :navigation="{
      prevEl: '.swiper-button-prev',
      nextEl: '.swiper-button-next',
    }"
    :modules="[Navigation]"
    class="mySwiper"
  >
    <SwiperSlide
      v-for="(movie, index) in movies"
      :key="index"
      @mouseover="getGenre(movie.id)"
    >
    <img
          :src="`https://image.tmdb.org/t/p/w500/${movie.backdrop_path}`"
          alt=""
        />
        <div class="buttons">
          <div class="buttons--left">
            <button class="button button-play">
              <NuxtLink :to="`/movies/${movie.id}`">
                <font-awesome :icon="['fas', 'play']" class="icon" />
              </NuxtLink>
            </button>
            <button class="button">
              <font-awesome :icon="['fas', 'plus']" class="icon" />
            </button>
            <button class="button">
              <font-awesome :icon="['fas', 'thumbs-up']" class="icon" />
            </button>
          </div>
        </div>
        <div class="rate-title">
          <div class="title">
            <p>
              {{ movie.original_title.slice(0, 20) }}
              <span v-if="movie.title.length > 20">...</span>
            </p>
          </div>
          <div class="rate">
            <span>
              <font-awesome :icon="['fas', 'star']" class="icon-star" />
            </span>
            <p>{{ movie.vote_average.toFixed(1) }}</p>
          </div>
        </div>
        <div class="genres">
          <ul>
            <li v-for="(genre, index) in genres" :key="index">
              {{ genre.name }}
            </li>
          </ul>
        </div>
    </SwiperSlide>
    <div class="swiper-button-prev"></div>
    <div class="swiper-button-next"></div>
  </Swiper>
</template>

<script setup>
import { defineProps } from "vue";
import { Swiper, SwiperSlide } from "swiper/vue";
import { Navigation } from "swiper/modules";
import "swiper/css";
import "swiper/css/navigation";
import axios from "axios";
import { ref } from "vue";

const genres = ref([]);

const getGenre = async (id) => {
  try {
    const result = await axios.get(
      `https://api.themoviedb.org/3/movie/${id}?language=en-US`,
      {
        headers: {
          Authorization:
            "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMmRlYzI2ZDE5MDBmMWNmZjgzZjUwMGY3OTUxNzVlZCIsIm5iZiI6MTcxOTkxMTg1Ny44MTEzLCJzdWIiOiI2NTgzYjQ1NDE4MGRlYTUyYzM4YzNlNjgiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.sErLDbXdHrOZwK6ZYLc0EHxVyTldi_9dj1Bp3G0cK0I",
          accept: "application/json",
        },
      }
    );
    genres.value = result.data.genres;
    // console.log(genre.value)
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

const props = defineProps(["movies"]);
</script>

<style scoped>
a{
  color: black;
  text-decoration: none;
}
img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.swiper {
  width: 100%;
  height: 170px;
  overflow: visible;
}
@keyframes scaleAndHeightChange {
  0% {
    transform: scale(1);
    height: 170px;
  }
  50% {
    transform: scale(1.3);
    height: fit-content;
  }
  100% {
    transform: scale(1.3);
    height: fit-content;
  }
}

.swiper-slide {
  overflow: hidden;
  height: 170px;
  color: black;
  margin-right: 5px !important;
  background-color: var(--dark);
  text-align: center;
  align-content: center;
  border-radius: 5px;
  cursor: pointer;
  z-index: 1;
  animation: none;
}

.swiper-slide:hover {
  animation: scaleAndHeightChange 1.5s forwards;
  z-index: 3;
  box-shadow: 0px 3px 10px 3px rgba(0, 0, 0, 0.3);
}

.swiper-button-prev,
.swiper-button-next {
  z-index: 2;
  color: grey !important;
  border: grey !important;
}
.button {
  border-radius: 50%;
  width: 40px;
  height: 40px;
  background: var(--dark);
  border: 1px solid #8a939d;
  color: white;
  cursor: pointer;
  margin-right: 5px;
}

.button-play {
  padding-left: 3px;
  background: #fff;
  color: #000;
}

.buttons {
  margin: 20px 10px 10px 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.button:hover {
  border: 1px solid #fff;
}

.icon {
  justify-content: center;
  align-self: center;
  width: 17px;
  height: 17px;
}

.rate-title {
  color: #fff;
  display: flex;
  align-items: center;
  text-align: center;
  margin: 20px 0 0 10px;
}

.title {
  margin-right: 15px;
  flex-wrap: wrap;
}

.rate {
  display: flex;
}

.rate p {
  margin-left: 5px;
}

.icon-star {
  color: yellow;
}

.genres {
  margin: 0px 10px 10px 10px;
  color: #fff;
}

.genres ul {
  list-style-type: none;
  display: flex;
  padding: 0;
  margin: 0;
  flex-wrap: wrap;
}

.genres li {
  margin: 0 10px 0 0;
}
</style>
