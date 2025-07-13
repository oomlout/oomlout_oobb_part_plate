$fn = 50;


union() {
	translate(v = [0, 0, 0]) {
		projection() {
			intersection() {
				translate(v = [-500, -500, -1.5000000000]) {
					cube(size = [1000, 1000, 0.1000000000]);
				}
				difference() {
					union() {
						hull() {
							translate(v = [-137.0000000000, 2.0000000000, 0]) {
								cylinder(h = 6, r = 5);
							}
							translate(v = [137.0000000000, 2.0000000000, 0]) {
								cylinder(h = 6, r = 5);
							}
							translate(v = [-137.0000000000, -2.0000000000, 0]) {
								cylinder(h = 6, r = 5);
							}
							translate(v = [137.0000000000, -2.0000000000, 0]) {
								cylinder(h = 6, r = 5);
							}
						}
					}
					union() {
						translate(v = [-135.0000000000, 0.0000000000, 0]) {
							cylinder(h = 6, r = 3.0000000000);
						}
						translate(v = [-135.0000000000, 0.0000000000, 0]) {
							cylinder(h = 6, r = 1.5000000000);
						}
						translate(v = [-135.0000000000, 0.0000000000, 0]) {
							cylinder(h = 6, r = 1.5000000000);
						}
						translate(v = [-135.0000000000, 0.0000000000, 0]) {
							cylinder(h = 6, r = 1.5000000000);
						}
					}
				}
			}
		}
	}
	translate(v = [0, 24, 0]) {
		projection() {
			intersection() {
				translate(v = [-500, -500, 1.5000000000]) {
					cube(size = [1000, 1000, 0.1000000000]);
				}
				difference() {
					union() {
						hull() {
							translate(v = [-137.0000000000, 2.0000000000, 0]) {
								cylinder(h = 6, r = 5);
							}
							translate(v = [137.0000000000, 2.0000000000, 0]) {
								cylinder(h = 6, r = 5);
							}
							translate(v = [-137.0000000000, -2.0000000000, 0]) {
								cylinder(h = 6, r = 5);
							}
							translate(v = [137.0000000000, -2.0000000000, 0]) {
								cylinder(h = 6, r = 5);
							}
						}
					}
					union() {
						translate(v = [-135.0000000000, 0.0000000000, 0]) {
							cylinder(h = 6, r = 3.0000000000);
						}
						translate(v = [-135.0000000000, 0.0000000000, 0]) {
							cylinder(h = 6, r = 1.5000000000);
						}
						translate(v = [-135.0000000000, 0.0000000000, 0]) {
							cylinder(h = 6, r = 1.5000000000);
						}
						translate(v = [-135.0000000000, 0.0000000000, 0]) {
							cylinder(h = 6, r = 1.5000000000);
						}
					}
				}
			}
		}
	}
}