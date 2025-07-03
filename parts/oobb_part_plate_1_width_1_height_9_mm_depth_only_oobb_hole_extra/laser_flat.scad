$fn = 50;


union() {
	translate(v = [0, 0, 0]) {
		projection() {
			intersection() {
				translate(v = [-500, -500, -3.0000000000]) {
					cube(size = [1000, 1000, 0.1000000000]);
				}
				difference() {
					union() {
						cylinder(h = 9, r = 7.0000000000);
					}
					union() {
						translate(v = [0, 0, -100]) {
							cylinder(h = 200, r = 3.0000000000);
						}
					}
				}
			}
		}
	}
	translate(v = [0, 24, 0]) {
		projection() {
			intersection() {
				translate(v = [-500, -500, 0.0000000000]) {
					cube(size = [1000, 1000, 0.1000000000]);
				}
				difference() {
					union() {
						cylinder(h = 9, r = 7.0000000000);
					}
					union() {
						translate(v = [0, 0, -100]) {
							cylinder(h = 200, r = 3.0000000000);
						}
					}
				}
			}
		}
	}
	translate(v = [0, 48, 0]) {
		projection() {
			intersection() {
				translate(v = [-500, -500, 3.0000000000]) {
					cube(size = [1000, 1000, 0.1000000000]);
				}
				difference() {
					union() {
						cylinder(h = 9, r = 7.0000000000);
					}
					union() {
						translate(v = [0, 0, -100]) {
							cylinder(h = 200, r = 3.0000000000);
						}
					}
				}
			}
		}
	}
}