from apiwrapper.endpoints.monetary_account import MonetaryAccount


class Schedule(MonetaryAccount):

    endpoint_schedule = "schedule"
    endpoint_schedule_instance = "schedule-instance"

    @classmethod
    def get_base_endpoint(cls, user_id, account_id, schedule_id=None):
        endpoint = MonetaryAccount.get_base_endpoint(user_id, account_id)
        endpoint += "/%s" % cls.endpoint_schedule
        if schedule_id is not None:
            endpoint += "/%d" % schedule_id
        return endpoint

    # Schedule Logic
    def get_all_schedules_for_account(self, user_id, account_id):
        endpoint = self.get_base_endpoint(user_id, account_id)

        return self._make_get_request(endpoint)

    def get_schedule_by_id(self, user_id, account_id, schedule_id):
        endpoint = self.get_base_endpoint(user_id, account_id, schedule_id)

        return self._make_get_request(endpoint)

    def get_all_schedules_for_user(self, user_id):
        endpoint = "/%s/%d/%s" % (
            self.endpoint_user,
            user_id,
            self.endpoint_schedule
        )
        return self._make_get_request(endpoint)

    # Schedule Instance Logic
    def get_all_instances_for_schedule(self, user_id, account_id, schedule_id):
        endpoint = self.get_base_endpoint(user_id, account_id, schedule_id)
        endpoint += "/%s" % self.endpoint_schedule_instance

        return self._make_get_request(endpoint)

    def get_schedule_instance_by_id(self, user_id, account_id, schedule_id,
                                    instance_id):
        endpoint = self.get_base_endpoint(user_id, account_id, schedule_id)
        endpoint += "/%s/%d" % (
            self.endpoint_schedule_instance,
            instance_id
        )

        return self._make_get_request(endpoint)


