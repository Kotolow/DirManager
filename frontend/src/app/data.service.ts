import { Injectable } from '@angular/core';
import { HttpClient, HttpParams} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  private REST_API_SERVER = "http://localhost:8000/files";

  constructor(private httpClient: HttpClient) { }

  public sendGetRequest(){
    return this.httpClient.get<any[]>(this.REST_API_SERVER);
  }

  public getFilteredResults(filterValue: string){
    let params = new HttpParams().set('filter', filterValue);
    return this.httpClient.get<any[]>('http://localhost:8000/filtered_files/', { params: params });
  }
}
