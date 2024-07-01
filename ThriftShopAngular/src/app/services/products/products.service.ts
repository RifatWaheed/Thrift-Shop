import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { URLService } from '../url/url.service';
import { Product } from '../../models/product/product';

@Injectable({
    providedIn: 'root'
})
export class ProductsService {

    private contactInfoURL = 'http://127.0.0.1:8000/contactInfo'; // Replace with your API URL

    constructor(
        private http: HttpClient,
        private urlService : URLService,
    ) { }

    createProduct(param : Product): Observable<any> {
        return this.http.post(this.urlService.concatEndpointLocal("createProduct"), param);
    }
}
