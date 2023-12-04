import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  files: any[] = [];
  filterValue: string = '';

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    this.dataService.sendGetRequest().subscribe((data: any[])=>{
      this.files = data;
    })
  }

  applyFilter(){
    if(this.filterValue === ''){
      this.dataService.sendGetRequest().subscribe((data: any[])=>{
        this.files = data;
      })
    } else {
      this.dataService.getFilteredResults(this.filterValue).subscribe((data: any[])=>{
        this.files = data;
      })
    }
  }

}
