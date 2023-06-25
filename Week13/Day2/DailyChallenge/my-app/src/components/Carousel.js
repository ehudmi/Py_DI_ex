import React, { Component } from 'react';
import "react-responsive-carousel/lib/styles/carousel.min.css"; // requires a loader
import { Carousel } from 'react-responsive-carousel';
import vegas from './assets/Vegas.webp';
import japan from './assets/3.webp';
import hong from './assets/Hong.jpg';
import macao from './assets/Macao.webp';

class DemoCarousel extends Component {
    render() {
        return (
            <Carousel>
                <div>
                    <img src={hong} />
                    <p className="legend">Hong Kong</p>
                </div>
                <div>
                    <img src={macao} />
                    <p className="legend">Macao</p>
                </div>
                <div>
                    <img src={japan} />
                    <p className="legend">Japan</p>
                </div>
                <div>
                    <img src={vegas}></img>
                    <p className="legend">Las Vegas</p>
                </div>
            </Carousel>
        );
    }
};

export default DemoCarousel;