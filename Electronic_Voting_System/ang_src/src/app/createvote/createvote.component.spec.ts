import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CreatevoteComponent } from './createvote.component';

describe('CreatevoteComponent', () => {
  let component: CreatevoteComponent;
  let fixture: ComponentFixture<CreatevoteComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreatevoteComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreatevoteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
