import { NgModule } from '@angular/core';

import { Routes, RouterModule } from '@angular/router';


import{HomeComponent} from './components/home/home.component'; 
import{PublicvoteeventsComponent} from './components/publicvoteevents/publicvoteevents.component'; 
import{RegisterComponent} from './components/register/register.component'; 
import{SigninComponent} from './components/signin/signin.component'; 
import{PagenotfoundComponent} from './components/pagenotfound/pagenotfound.component'; 
import{HomelogComponent} from './homelog/homelog.component';
import{MyvoteComponent} from './myvote/myvote.component';
import{CreatevoteComponent} from './createvote/createvote.component';









const routes: Routes = [
   { path: 'home', component: HomeComponent },
  { path: 'publicvoteevents',      component:PublicvoteeventsComponent },
  {path: 'register', component:RegisterComponent},
  {path: 'signin',component:SigninComponent},
  { path: 'pagenotfound', component: PagenotfoundComponent },
 {path: 'Homelog',component:HomelogComponent},
{path:'myvote',component:MyvoteComponent},
{path:'createvote',component:CreatevoteComponent}
];


@NgModule({

  imports: [RouterModule.forRoot(routes)],

  exports: [RouterModule]

})

export class AppRoutingModule { }

export const routingComponents=[HomeComponent,PublicvoteeventsComponent,RegisterComponent,SigninComponent,PagenotfoundComponent,HomelogComponent,MyvoteComponent,CreatevoteComponent]