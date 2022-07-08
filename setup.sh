#!/bin/bash
export ASSISTANT_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVOX3hfRldDczV2N295WHB3MXhCUiJ9.eyJpc3MiOiJodHRwczovL3Rlc3RhdXRoLWNqLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MmM0NjNjZjhhMDZjNTc2YjM3MWYyZTQiLCJhdWQiOiJmc25kLWNhcHN0b25lIiwiaWF0IjoxNjU3Mjk0NTcwLCJleHAiOjE2NTczODA5NzAsImF6cCI6Ilo4ZWd4cnJjdDI1NjVnQk91c0hpQnpuRmgxcmc5VWkxIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.A2CLCuzbg_w13PlPGJYDvZffsX3ySkZQ50dXz1iFUNpzC15bKrN8LPLiEZ8JZc1WX3zDq1Vq9iZ_wGhcEPZmvdw4RMVd4heTprSEce1i0oykuD8JM7FVQ5G5v6GZtkUocSJHDQY6mJiGwhzw7YOtbMxvXaiZhjs3sAOrHgnxWjTQkGa0viRI_1vyKOvgho2tr91l36D1FiYVUzsiCrGjOsrfakwMPBaTCHxi1Zy1luZFf1QgtlZQsLqekYP1d9-VZSDwDkud8ZzzWoi6hkBZuNWSdS5H8wfdrhUJ3dvGVrEn5e3oaKLGWkVt1FY3xFqGUei_AV0DQzHJjNP8bx3kSw"
export DIRECTOR_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVOX3hfRldDczV2N295WHB3MXhCUiJ9.eyJpc3MiOiJodHRwczovL3Rlc3RhdXRoLWNqLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MmM0NjQ3NThhMDZjNTc2YjM3MWYzMDAiLCJhdWQiOiJmc25kLWNhcHN0b25lIiwiaWF0IjoxNjU3Mjk0NjE0LCJleHAiOjE2NTczODEwMTQsImF6cCI6Ilo4ZWd4cnJjdDI1NjVnQk91c0hpQnpuRmgxcmc5VWkxIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.HStsb9vZ06UGXQE-9V83crpikHcORAaSC2UpzTMdwxEWrvKyjusBRcBWyJ7olGre4uATLUlR9ZDSES_pJAsGU2vC938ejejvpMyRszYgDM0WMzm3vt_sQwb_S7duY1Tr_w7kDl9logkKdgBTf6gO8IKvqGQMQ8SKQBj4kkfTRAYmATIG_VA0PFgzyspWtyAKhSMtKHPBDQy8OI3HqdYBe-juEhfSYewxYKrqeeNiDq04VU2DhWhDgk1RvvYIz0bXs7tva9Y31RU-is2k2kRBjgIzW-cLpIsl3ECUDidR8YgB2jjo5pIyPbfUz7pC0-rsC80kVOTscMeFzasyqWKukA"
export PRODUCER_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVOX3hfRldDczV2N295WHB3MXhCUiJ9.eyJpc3MiOiJodHRwczovL3Rlc3RhdXRoLWNqLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MmM0NjRkNDhhMDZjNTc2YjM3MWYzMjYiLCJhdWQiOiJmc25kLWNhcHN0b25lIiwiaWF0IjoxNjU3MjkyNDU3LCJleHAiOjE2NTczNzg4NTcsImF6cCI6Ilo4ZWd4cnJjdDI1NjVnQk91c0hpQnpuRmgxcmc5VWkxIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.pV_SqTwrFPKm4AEp3rVPWVpuan67FcC3LWTpMAHzHGyw98zO4Am7-s69_QHjWVG-XavUJZQsMKjoTg9etdmKa7q12IpXg4QzH4Q2_AbMdYYlQL_hvnlOY_vXZXI3Z8AIoKauKMALbV_4T-c_BdlJpkZadaWsLneI97IcIxhMnJXS13r9BmzU7y7kLj0dw0fv5XfPS8wvmV0VGLsGP5GWoXkyQmZjO7aN_IM-9kullOevm1b4rmOzhhDsgsX8HtP_OGSAcIKhDOHO0x8WKsgRV0g1OJbtiW1MMyMH6BxdvzU1Zp8_XS7_0QzzMOog2aDqbHIWMOhZPE1CicMDj-is0A"
echo "setup.sh script executed successfully!"