<template>
  <div class="container">
    <div class="player" v-if="movieKey">
      <player-youtube :id_movie="movieKey" />
    </div>
    <div class="placeholder-image" v-else>
      <img
        :src="`https://image.tmdb.org/t/p/w500/${movie.backdrop_path}`"
        alt=""
      />
    </div>
    <div class="movie-detail" v-if="movie">
      <div class="movie-content--left">
        <h3>{{ movie.title }}  {{ movie.tagline }}</h3>
        <div class="rate">
          <span>
            <font-awesome :icon="['fas', 'star']" class="icon-star" />
          </span>
          <p class="average">
            {{ movie.vote_average ? movie.vote_average.toFixed(1) : "N/A" }}
          </p>
          <p class="count">({{ movie.vote_count }})</p>
        </div>
        <div
          class="year-country"
          v-if="movie.release_date && movie.origin_country"
        >
          <span
            >{{ movie.release_date.split("-")[0] }} -
            {{ movie.origin_country[0] }}</span
          >
        </div>
        <div class="genres">
          <ul>
            <li v-for="(genre, index) in movie.genres" :key="index">
              {{ genre.name }}
            </li>
          </ul>
        </div>
        <div class="description">
          <p>{{ movie.overview }}</p>
        </div>
      </div>
    </div>
    <div v-if="moviesRecommended.length > 0">
      <h2>Recommend</h2>
      <br />
      <SwiperComponent :movies="moviesRecommended" />
    </div>
    <div class="block"></div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import "@/assets/styles/global.css";
import PlayerYoutube from "@/components/PlayerYoutube.vue";
import SwiperComponent from "@/components/SwiperComponent.vue";

const { id } = useRoute().params;
const movie = ref({});
const movieKey = ref(null);
const moviesRecommended = ref([]);

definePageMeta({
  layout: "main",
})

const recommendMovies = async (id) => {
  try {
    const result = await axios.get(
      `https://api.themoviedb.org/3/movie/${id}/recommendations?language=en-US&page=1`,
      {
        headers: {
          Authorization:
            "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMmRlYzI2ZDE5MDBmMWNmZjgzZjUwMGY3OTUxNzVlZCIsIm5iZiI6MTcxOTkxMTg1Ny44MTEzLCJzdWIiOiI2NTgzYjQ1NDE4MGRlYTUyYzM4YzNlNjgiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.sErLDbXdHrOZwK6ZYLc0EHxVyTldi_9dj1Bp3G0cK0I",
          accept: "application/json",
        },
      }
    );
    moviesRecommended.value = result.data.results;
    console.log("recommend", moviesRecommended.value);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

const getIdMovieVideo = async (id) => {
  try {
    const result = await axios.get(
      `https://api.themoviedb.org/3/movie/${id}/videos?language=en-US`,
      {
        headers: {
          Authorization:
            "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMmRlYzI2ZDE5MDBmMWNmZjgzZjUwMGY3OTUxNzVlZCIsIm5iZiI6MTcxOTkxMTg1Ny44MTEzLCJzdWIiOiI2NTgzYjQ1NDE4MGRlYTUyYzM4YzNlNjgiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.sErLDbXdHrOZwK6ZYLc0EHxVyTldi_9dj1Bp3G0cK0I",
          accept: "application/json",
        },
      }
    );

    // Filter for the first object with type 'Trailer'
    const trailer = result.data.results.find(
      (video) => video.type === "Trailer"
    );

    if (trailer) {
      movieKey.value = trailer.key;
      console.log(movieKey.value);
    } else {
      console.warn("No trailer found for the movie.");
    }
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

const getMovieDetail = async (id) => {
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
    movie.value = result.data;
    console.log("movie-detail", movie.value);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};
onMounted(() => {
  getMovieDetail(id);
  getIdMovieVideo(id);
  recommendMovies(id);
});
</script>

<style scoped>
/* .container {

} */
.placeholder-image img{
  width: 100%;
  height: auto;
  object-fit: cover;
}
.movie-detail {
  margin-top: 30px;
  width: 100%;
  height: fit-content;
  padding-bottom: 10px;
  /* background: blue; */
  display: flex;
  justify-content: space-between;
}
.rate {
  text-align: center;
  display: inline-flex;
  background: #2c2c2c;
  padding: 5px 10px;
  border-radius: 10px;
}
.average {
  font-size: 20px;
  margin: 0;
  font-weight: 500;
}
.count {
  color: #616161;
  font-size: 20px;
  margin: 0 0 0 5px;
}
.rate span {
  height: fit-content;
}
.icon-star {
  color: yellow;
  margin: 7px 5px 0 0;
}
.year-country {
  margin-top: 10px;
  font-size: 18px;
}

.genres {
  margin-top: 10px;
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
  margin: 0 20px 0 0;
}

.movie-content--left {
  height: fit-content;
  width: 60%;
}
.description {
  margin-top: 10px;
}

.actor-director-genre {
  display: inline-flex;
}
.swiper-wrapper {
  position: relative;
  z-index: 1;
}
.swiper-wrapper:hover {
  z-index: 3;
}
.block {
  height: 400px;
}
</style>