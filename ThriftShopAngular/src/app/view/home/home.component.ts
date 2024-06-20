import { Component, OnInit } from '@angular/core';
import { NgbCarouselModule } from '@ng-bootstrap/ng-bootstrap';
import { CarouselImage } from '../../models/carouselImage/carousel';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'home',
  standalone: true,
  imports:  [NgbCarouselModule,CommonModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent implements OnInit {
  
  carouselImages : CarouselImage[] = [];

  constructor(){

  }

  ngOnInit(): void {
    this.processCarouselImages();    
  }

  processCarouselImages() {
    this.carouselImages = [
        {src : "assets/images/carousel_images/keyboards.png", alt:"keyboard"},
        {src : "assets/images/carousel_images/mouse3.png", alt:"keyboard"}
    ];
  }



}
