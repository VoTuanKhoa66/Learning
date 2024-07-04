<template>
  <div class="container">
    <img
      src="https://m.media-amazon.com/images/M/MV5BODAwM2Q4YTMtYjc0ZC00NjcwLWIwMTAtZDkwYzI3Y2ZlYWI3XkEyXkFqcGc@._V1_.jpg"
      alt=""
      class="thumbnail"
    />
    <div class="thumbnail-content">
      <h1>UNDER PARIS</h1>
      <p>
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Repudiandae
        amet mollitia quos laudantium libero animi optio totam est debitis ea
        quam maiores, fuga cum aut numquam saepe vitae reiciendis et!
      </p>
      <div class="buttons">
        <button type="button" class="btn btn-light play-button">
          <font-awesome :icon="['fas', 'play']" />
          <span>Play</span>
        </button>
        <button type="button" class="btn btn-secondary infor-button">
          <font-awesome :icon="['fas', 'circle-info']" />
          <span>More Infor</span>
        </button>
      </div>
    </div>
    <div class="list-movies">
      <h2>Movies</h2>
      <div v-if="movies.length > 0" class="swiper-wrapper">
        <SwiperComponent :movies="movies" />
      </div>
      <h2>Popular</h2>
      <div v-if="popularMovie.length > 0" class="swiper-wrapper">
        <SwiperComponent :movies="popularMovie" />
      </div>
      <h2>Top Rated</h2>
      <div v-if="topRateMovie.length > 0" class="swiper-wrapper">
        <SwiperComponent :movies="topRateMovie" />
      </div>
      <h2>Upcoming</h2>
      <div v-if="topRateMovie.length > 0" class="swiper-wrapper">
        <SwiperComponent :movies="upComing" />
      </div>
      <div class="block"></div>
    </div>
  </div>
</template>

<script setup>
import SwiperComponent from "../components/SwiperComponent.vue";
import axios from "axios";
import { ref, onMounted, onUpdated } from "vue";

definePageMeta({
  layout: "main",
})

const movies = ref([]);
const popularMovie = ref([]);
const topRateMovie = ref([]);
const upComing = ref([]);



const getMovies = async () => {
  try {
    const result = await axios.get(
      "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1",
      {
        headers: {
          Authorization:
            "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMmRlYzI2ZDE5MDBmMWNmZjgzZjUwMGY3OTUxNzVlZCIsIm5iZiI6MTcxOTkxMTg1Ny44MTEzLCJzdWIiOiI2NTgzYjQ1NDE4MGRlYTUyYzM4YzNlNjgiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.sErLDbXdHrOZwK6ZYLc0EHxVyTldi_9dj1Bp3G0cK0I",
          accept: "application/json",
        },
      }
    );
    movies.value = result.data.results;
    console.log(movies.value);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

const getPopularMovies = async () => {
  try {
    const result = await axios.get(
      "https://api.themoviedb.org/3/movie/popular?language=en-US&page=2",
      {
        headers: {
          Authorization:
            "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMmRlYzI2ZDE5MDBmMWNmZjgzZjUwMGY3OTUxNzVlZCIsIm5iZiI6MTcxOTkxMTg1Ny44MTEzLCJzdWIiOiI2NTgzYjQ1NDE4MGRlYTUyYzM4YzNlNjgiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.sErLDbXdHrOZwK6ZYLc0EHxVyTldi_9dj1Bp3G0cK0I",
          accept: "application/json",
        },
      }
    );
    popularMovie.value = result.data.results;
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

const getTopRateMovies = async () => {
  try {
    const result = await axios.get(
      "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=3",
      {
        headers: {
          Authorization:
            "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMmRlYzI2ZDE5MDBmMWNmZjgzZjUwMGY3OTUxNzVlZCIsIm5iZiI6MTcxOTkxMTg1Ny44MTEzLCJzdWIiOiI2NTgzYjQ1NDE4MGRlYTUyYzM4YzNlNjgiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.sErLDbXdHrOZwK6ZYLc0EHxVyTldi_9dj1Bp3G0cK0I",
          accept: "application/json",
        },
      }
    );
    topRateMovie.value = result.data.results;
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

const getUpcoming = async () => {
  try {
    const result = await axios.get(
      "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=4",
      {
        headers: {
          Authorization:
            "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMmRlYzI2ZDE5MDBmMWNmZjgzZjUwMGY3OTUxNzVlZCIsIm5iZiI6MTcxOTkxMTg1Ny44MTEzLCJzdWIiOiI2NTgzYjQ1NDE4MGRlYTUyYzM4YzNlNjgiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.sErLDbXdHrOZwK6ZYLc0EHxVyTldi_9dj1Bp3G0cK0I",
          accept: "application/json",
        },
      }
    );
    upComing.value = result.data.results;
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

// Call getMovies when the component is mounted
onMounted(() => {
  getMovies();
  getPopularMovies();
  getTopRateMovies();
  getUpcoming();
});

// Update Swiper after data is loaded
onUpdated(() => {
  // Trigger update event for Swiper
  document.querySelectorAll(".mySwiper").forEach((swiper) => {
    swiper.swiper.update();
  });
});
</script>

<style scoped>
.container {
  position: relative;
  padding: 0;
  max-width: 100%;
}
.container img {
  z-index: 0;
  height: auto;
  max-width: 100%;
  width: 100%;
}
.thumbnail-content {
  z-index: 1;
  color: white;
  position: absolute;
  top: 0;
  padding-left: 110px;
  padding-top: 20%;
  width: 100%;
}
.list-movies {
  position: absolute;
  padding-left: 110px;
  width: 100%;
  top: 85%;
}
.list-movies h2 {
  margin: 20px 0 20px 0;
}
.swiper-wrapper {
  position: relative;
  z-index: 1;
}
.swiper-wrapper:hover {
  z-index: 3;
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
  background-color: rgba(189, 195, 199, 0.7);
  align-items: center;
  width: 170px;
  margin-right: 10px;
  padding: 10px;
  font-size: 18px;
  font-weight: 600;
  border: none;
}

.infor-button:hover {
  background-color: rgba(189, 195, 199, 0.4);
  border: none;
}

.icon {
  width: 22px !important;
  height: 22px !important;
}
.block {
  height: 400px;
}
</style>
