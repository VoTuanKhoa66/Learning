<template>
  <Carousel :items-to-show="4.5" :wrap-around="true">
    <Slide v-for="movie in movies" :key="movie">
      <div class="carousel__item">
        <img :src="movie.image_url" alt="">
      </div>
    </Slide>

    <template #addons>
      <Navigation />
    </template>
  </Carousel>
</template>
  
<script setup>
// import { reactive } from "vue";
import "vue3-carousel/dist/carousel.css";
import "../assets/styles/carousel-styles.css";
import { Carousel, Slide, Navigation } from "vue3-carousel";

// Dynamic import for images
// const images = import.meta.glob('../assets/images/*.{jpg,jpeg,png}', { eager: true });

// Sample data for movies
// const movies = reactive([
//   { name: "Movie 1", image_url: images['../assets/images/image1.jpg'].default },
//   { name: "Movie 2", image_url: images['../assets/images/image2.jpeg'].default },
//   { name: "Movie 3", image_url: images['path/to/image3.jpg'] ? images['path/to/image3.jpg'].default : 'fallback.jpg' },
//   { name: "Movie 4", image_url: images['path/to/image4.jpg'] ? images['path/to/image4.jpg'].default : 'fallback.jpg' },
//   { name: "Movie 5", image_url: images['path/to/image5.jpg'] ? images['path/to/image5.jpg'].default : 'fallback.jpg' },
//   { name: "Movie 6", image_url: images['path/to/image6.jpg'] ? images['path/to/image6.jpg'].default : 'fallback.jpg' },
//   { name: "Movie 7", image_url: images['path/to/image7.jpg'] ? images['path/to/image7.jpg'].default : 'fallback.jpg' },
//   { name: "Movie 8", image_url: images['path/to/image8.jpg'] ? images['path/to/image8.jpg'].default : 'fallback.jpg' },
//   { name: "Movie 9", image_url: images['path/to/image9.jpg'] ? images['path/to/image9.jpg'].default : 'fallback.jpg' },
//   { name: "Movie 10", image_url: images['path/to/image10.jpg'] ? images['path/to/image10.jpg'].default : 'fallback.jpg' },
// ]);

</script>

<style scoped>
.carousel__item {
  height: 200px;
  width: 100%;
  background-color: var(--vc-clr-primary);
  color: var(--vc-clr-white);
  font-size: 20px;
  border-radius: 16px;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
}

.carousel__item img{
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.carousel__item:hover{
  transform: scale(1.5);
  cursor: pointer;
}


.carousel__slide {
  z-index: 3;
  padding: 5px;
}

.carousel__prev,
.carousel__next {
  box-sizing: content-box;
  border: 5px solid white;
}

</style>
