import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { LOCAL_BASE_URL } from '../../../environment/enviornment.dev';


@Injectable({
    providedIn: 'root'
})
export class URLService {

    constructor(
        private http: HttpClient,
    ) { }

    concatEndpointLocal(endpoint: string): string {
        endpoint = LOCAL_BASE_URL + endpoint;
        return endpoint;
    }
}
