import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PublicvoteeventsComponent } from './publicvoteevents.component';

describe('PublicvoteeventsComponent', () => {
  let component: PublicvoteeventsComponent;
  let fixture: ComponentFixture<PublicvoteeventsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PublicvoteeventsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PublicvoteeventsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
