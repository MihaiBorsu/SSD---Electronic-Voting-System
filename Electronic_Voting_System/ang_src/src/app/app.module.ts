import { RouterModule, Routes } from '@angular/router';
import { BrowserModule } from '@angular/platform-browser';

import { NgModule } from '@angular/core';


import { AppRoutingModule,routingComponents } from './app-routing.module';


import { AppComponent } from './app.component';

import {MatButtonModule,MatCheckboxModule,MatToolbarModule} from '@angular/material';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {FormsModule,ReactiveFormsModule} from '@angular/forms';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatInputModule} from '@angular/material/input';
import { HomelogComponent } from './homelog/homelog.component';
import { LogoutComponent } from './logout/logout.component';
import { MyvoteComponent } from './myvote/myvote.component';
import { CreatevoteComponent } from './createvote/createvote.component';
import {MatSelectModule} from '@angular/material/select';

const appRoutes: Routes = [
 
];



@NgModule({
  declarations: [
 
   AppComponent
 ,
   routingComponents,
   HomelogComponent,
   LogoutComponent,
   MyvoteComponent,
   CreatevoteComponent
],
 
 imports: [
 
   BrowserModule,
  
   MatButtonModule,
   MatCheckboxModule,
   MatToolbarModule,
   RouterModule.forRoot(appRoutes),
    AppRoutingModule,
    MatFormFieldModule,
    MatInputModule,
    FormsModule,
    ReactiveFormsModule,
    MatSelectModule
  
],
    providers: [],
  
bootstrap: [AppComponent]


})

export class AppModule { }
